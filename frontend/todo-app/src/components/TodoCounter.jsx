import React from 'react'

function TodoCounter({completed, total}) {
    return (
        <p>Haz completado {completed || '0'} de {total || '0'} tareas</p>
    )
}

export {TodoCounter}