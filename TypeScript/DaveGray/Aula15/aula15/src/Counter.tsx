import { type ReactNode } from "react";
import { useCounter, useCounterText } from "./context/CounterContext";

type ChildrenType = {
    children: (num: number) => ReactNode,
}
        
const Counter = ({children}: ChildrenType) => {
    const { count, increment, decrement} = useCounter()
    const {text, handleTextInput} = useCounterText()
    

    return (
        <div>
            <h1>{children(count)}</h1>
            <div>
                <button onClick={increment}>+</button>
                <button onClick={decrement}>-</button>
                <input type="text" onChange={handleTextInput}></input>
                <h2>{text}</h2>
            </div>
        </div>
    )
}

export default Counter