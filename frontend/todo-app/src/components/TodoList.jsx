import React from 'react'

function TodoList(props) {
  return (
    <ul className='list-group d-flex justify-content-center'>
        {props.children}
    </ul>
  )
}

export {TodoList}