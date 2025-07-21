 import { useContext } from "react";
 import ProductsContext from "../context/ProductsProvider";
 import { type UseProductsContextType } from "../context/ProductsProvider";
 
 const useProducts = (): UseProductsContextType => {
     return useContext(ProductsContext)
 }
 
 export default useProducts