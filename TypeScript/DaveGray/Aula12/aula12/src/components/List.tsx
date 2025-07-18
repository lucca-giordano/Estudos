import { type ReactNode } from "react";

interface ListProps<T>{
    items: T[],
    render: (item: T) => ReactNode
}

const List = <T,>({ items, render}: ListProps<T>) => {
  return (
    <div>
        <ul>
            {items.map((item, i) => (
                <li key={i}>
                    {render(item)}
                </li>
            ))}
        </ul>
    </div>
  )
}

export default List