import React from "react";

function TodoItem(props) {
  return (
    <li className={`${props.completed ? 'alert-success' : 'alert-light'} alert alert-dismissible py-1 d-flex align-items-center text-start fade show`}>
        <span className="fs-3" onClick={props.onCompleted}>
          <i
            className={`bi ${
              props.completed ? "bi-check-circle-fill" : "bi-circle"
            } me-2`}
          >
          </i>
        </span>
      <span className={`${props.completed ? 'fst-italic text-decoration-line-through' : ''}`}>
        {props.text || ""}
      </span>
      <button type="button" className="btn-close" onClick={props.onDeleted}></button>
    </li>
  );
}

export { TodoItem };
