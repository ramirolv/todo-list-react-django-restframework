import { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-icons/font/bootstrap-icons.min.css";
import { TodoCounter } from "./components/TodoCounter";
import { TodoSearch } from "./components/TodoSearch";
import { TodoList } from "./components/TodoList";
import { TodoItem } from "./components/TodoItem";
import { CreateItemButton } from "./components/CreateItemButton";

function useLocalState(itemName, initialValue){
  const getStorage = () => JSON.parse(localStorage.getItem(itemName)) || initialValue;

  const [items, setItems] = useState(getStorage());

  const updateStorage = (itemsArray) => {
    localStorage.setItem(itemName, JSON.stringify(itemsArray));
  };
  
  const updateItems = (newItemsArray) => {
    setItems(newItemsArray);
    updateStorage(newItemsArray);
  };

  return [items, updateItems];
}

function App() {
  const [tasks, setTasks] = useLocalState("Tasks_V1", []);
  const [searchValue, setSearchValue] = useState("");
  const completedTodo = tasks.filter((todo) => !!todo.completed).length;
  const totalTodo = tasks.length;

  const searchedTodo = tasks.filter((task) => {
    return task.text.toLowerCase().includes(searchValue.toLowerCase());
  });

  const completeTodo = (text) => {
    const newTasks = [...tasks];
    const index = newTasks.findIndex((todo) => todo.text === text);
    newTasks[index].completed = !newTasks[index].completed;
    setTasks(newTasks);
  };

  const deleteTodo = (text) => {
    const newTasks = [...tasks];
    const index = newTasks.findIndex((todo) => todo.text === text);

    if (index !== -1) {
      newTasks.splice(index, 1);
      setTasks(newTasks);
    }
  };

  return (
    <main className="container-fluid p-5">
      <TodoCounter completed={completedTodo} total={totalTodo} />
      <div className="container">
        <TodoSearch searchValue={searchValue} setSearchValue={setSearchValue} />
      </div>
      <div className="col-md-10 mx-auto mt-5">
        <TodoList>
          {searchedTodo.map((todo) => (
            <TodoItem
              key={todo.text}
              text={todo.text}
              completed={todo.completed}
              onCompleted={() => completeTodo(todo.text)}
              onDeleted={() => deleteTodo(todo.text)}
            />
          ))}
        </TodoList>
      </div>
      <CreateItemButton />
    </main>
  );
}

export default App;
