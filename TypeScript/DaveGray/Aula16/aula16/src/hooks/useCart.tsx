import { useContext } from "react";
import CartContext from "../context/CartProvider";
import { type UseCartContextType } from "../context/CartProvider";

const useCart = (): UseCartContextType => {
    return useContext(CartContext)
}

export default useCart