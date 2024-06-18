import React from "react";

function TodoCounter(props) {
  return (
    <p>
      Haz completado {props.completed || "0"} de {props.total || "0"} tareas
    </p>
  );
}

export { TodoCounter };
