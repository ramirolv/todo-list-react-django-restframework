import React from "react";

function TodoItem(props) {
  return (
    <li className="list-group-item list-group-item-action alert alert-light d-flex align-items-center">
      <span>
        <i
          className={`bi ${
            props.completed ? "bi-check-circle-fill" : "bi-circle"
          } me-2`}
        >
          {" "}
        </i>
        {props.text || ""}
      </span>
      <button className="btn btn-sm btn-secondary rounded-pill p-0 position-absolute top-0 end-0 translate-middle">
        <i className="bi bi-x"></i>
      </button>
    </li>
  );
}

export { TodoItem };
