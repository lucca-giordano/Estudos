import Counter from "./Counter"

function App() {

  return (
    <div>
      <Counter>{(num: number) => <>Current count: {num}</>}</Counter>
    </div>
  )
}

export default App
