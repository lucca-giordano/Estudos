import Counter from "./Counter"
import { CounterProvider, initState } from "./context/CounterContext"

function App() {

  return (
    <div>
      <CounterProvider count={initState.count} text={initState.text}>
      <Counter>{(num: number) => <>Current count: {num}</>}</Counter>
      </CounterProvider>
    </div>
  )
}

export default App
