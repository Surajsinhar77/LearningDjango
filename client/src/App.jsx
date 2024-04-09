import { useState } from 'react'
import { useEffect } from 'react'
import './App.css'
import Signup from './components/Signup'

function App() {
  const [count, setCount] = useState(0)
  const[todos, setTodos] = useState([]);

  // useEffect(() => {
  //   fetch('http://127.0.0.1:8000/todos') // Replace '/api/todos' with your actual API endpoint
  //     .then(response => response.json())
  //     .then(data => setTodos(data))
  //     .catch(error => console.error(error));
  // }, []);
  return (
    <div>
      <Signup/>
    </div>
  )
}

export default App
