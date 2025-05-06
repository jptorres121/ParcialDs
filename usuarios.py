from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlmodel import Session, select

from models import Usuario, EstadoUsuario
from database import get_session

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.post("/", response_model=Usuario)
def crear_usuario(usuario: Usuario, session: Session = Depends(get_session)):
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario


@router.get("/", response_model=List[Usuario])
def listar_usuarios(session: Session = Depends(get_session)):
    return session.exec(select(Usuario)).all()


@router.get("/{usuario_id}", response_model=Usuario)
def obtener_usuario(usuario_id: int, session: Session = Depends(get_session)):
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


@router.put("/{usuario_id}/estado", response_model=Usuario)
def actualizar_estado_usuario(usuario_id: int, nuevo_estado: EstadoUsuario, session: Session = Depends(get_session)):
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    usuario.estado = nuevo_estado
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario


@router.put("/{usuario_id}/premium", response_model=Usuario)
def hacer_premium(usuario_id: int, session: Session = Depends(get_session)):
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    usuario.premium = True
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario


@router.get("/inactivos", response_model=List[Usuario])
def listar_inactivos(session: Session = Depends(get_session)):
    return session.exec(select(Usuario).where(Usuario.estado == EstadoUsuario.inactivo)).all()


@router.get("/premium-inactivos", response_model=List[Usuario])
def listar_premium_inactivos(session: Session = Depends(get_session)):
    return session.exec(
        select(Usuario).where(
            (Usuario.estado == EstadoUsuario.inactivo) & (Usuario.premium == True)
        )
    ).all()
