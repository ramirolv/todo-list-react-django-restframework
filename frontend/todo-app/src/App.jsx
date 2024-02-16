import { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-icons/font/bootstrap-icons.min.css";
import { TodoCounter } from "./components/TodoCounter";
import { TodoSearch } from "./components/TodoSearch";
import { TodoList } from "./components/TodoList";
import { TodoItem } from "./components/TodoItem";
import { CreateItemButton } from "./components/CreateItemButton";

const todoDefault = [
  {text: 'comer', completed: true},
  {text: 'dormir', completed: true},
  {text: 'correr', completed: true},
  {text: 'almorzar', completed: false},
]

function App() {
  const [tasks, setTasks] = useState(todoDefault);
  const [searchValue, setSearchValue] = useState('');
  const completedTodo = tasks.filter(todo => !!todo.completed).length;
  const totalTodo = tasks.length;

  return (
    <main className="container-fluid p-5">
      <TodoCounter completed={completedTodo} total={totalTodo} />
      <div className="container">
        <TodoSearch
        searchValue={searchValue}
        setSearchValue={setSearchValue}
        />
      </div>
      <div className="col-md-10 mx-auto mt-5">
        <TodoList>
          {todoDefault.map(todo => (
            <TodoItem
            key={todo.text}
            text={todo.text}
            completed={todo.completed}
            />
            ))}
        </TodoList>
      </div>
      <CreateItemButton />
    </main>
  );
}

export default App;
