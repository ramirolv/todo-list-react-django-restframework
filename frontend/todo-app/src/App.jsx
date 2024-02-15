import { useState } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-icons/font/bootstrap-icons.min.css'
import { TodoCounter } from './components/TodoCounter'
import { TodoSearch } from './components/TodoSearch'
import { TodoList } from './components/TodoList'
import { TodoItem } from './components/TodoItem'
import { CreateItemButton } from './components/CreateItemButton'


function App() {
  return (
    <>
      <main className="container-fluid p-5">
        <TodoCounter completed={15} total={20}/>
        <div className="container">
          <TodoSearch />
        </div>
        <div className='col-md-10 mx-auto mt-3'>
          <TodoList>
            <TodoItem />
            <TodoItem />
            <TodoItem />
            <TodoItem />
          </TodoList>
        </div>
        <CreateItemButton />
      </main>
    </>
  )
}

export default App
