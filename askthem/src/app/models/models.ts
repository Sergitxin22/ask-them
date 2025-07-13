export interface Usuario {
  id: number;
  username: string;
  password: string;
  monedas: number;
}

export interface Grupo {
  id: number;
  nombre: string;
  usuarios: number[];
}

export interface PreguntaAsignada {
  id: number;
  grupoId: number;
  preguntaId: number;
  fecha: string;
}

export interface Pregunta {
  id: number;
  pregunta: string;
  tipo: 'escrita' | 'seleccion-unica' | 'seleccion-multiple';
}

export interface Respuesta {
  id: number;
  usuarioId: number;
  grupoId: number;
  preguntaId: number;
  respuesta: string; // Para tipo 'escrita': texto libre
  usuariosSeleccionados?: number[]; // Para tipos 'seleccion-unica' y 'seleccion-multiple': IDs de usuarios
  fecha: string;
}
