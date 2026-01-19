from datetime import datetime
from typing import Optional, List, Annotated 
from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import SQLModel , Field , Session, create_engine, select

# Build Models
# We are making a Notepad application

class Note(SQLModel, table= True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    Content: str 
    is_done : bool = Field(default=False, index=True)
    created_at: datetime =  Field(default_factory=datetime.utcnow, index=True)

class NoteCreate(SQLModel):
    title: str
    content: str 

class NoteUpdate(SQLModel):
    title: Optional[str] = None
    content: Optional[str] = None
    is_done: Optional[str] = None 



# Building API stuff 

app= FastAPI(title="SQL MODEL STUFF")
engine = create_engine("sqlite:///./notes.db", echo=True)


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

# Building CRUD ROUTES

@app.post("/notes", response_model= Note)
def create_note(payload:NoteCreate, session: Session = Depends(get_session)):
    note = Note.model_validate(payload)
    session.add(note)
    session.commit()
    session.refresh(note)
    return note 

@app.get("/notes", response_model= List[Note])
def list_notes(is_done: Optional[bool]= None, session: Session= Depends(get_session)):
    note = select(Note)

    if is_done is not None:
        note = note.where(Note.is_done == is_done)

    note = note.order_by(Note.created_at.desc())
    return session.exec(note).all()

@app.get("/notes{note_id}", response_model= Note)
def get_note(note_id: int, session: Session= Depends(get_session)):
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found!")
    return note

@app.patch("/notes{note_id}", response_model= Note)
def update_note(note_id: int, payload:NoteUpdate, session: Session= Depends(get_session)):
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found!")
    
    updates = payload.model_dump(exclude_unset=True)
    for key, value in updates.items():
        setattr(note, key, value)

    session.add(note)
    session.commit()
    session.refresh(note)
    return note 


@app.delete("/notes/{note_id}")
def delete_note(note_id: int , session: Session= Depends(get_session)):
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found!")
    
    session.delete(note)
    session.commit()
    return {"message": "Delete the note succesfully! "}



