import ProductItem from './ProductItem';
import classes from './Products.module.css';
import { useEffect, useState } from 'react';

// const DUMMY_PRODUCTS = [
//   {
//     id: 1,
//     title: 'Test1',
//     price: 80.90,
//     description: 'This is the first dummy product'
//   },
//   {
//     id: 2,
//     title: 'Test2',
//     price: 380.90,
//     description: 'This is soon to be changed'
//   },
//   {
//     id: 3,
//     title: 'Test3',
//     price: 340.90,
//     description: 'First from the firebase'
//   },
//   {
//     id: 4,
//     title: 'Test4',
//     price: 150.2,
//     description: 'And soon from the Dj backend...'
//   },
// ];

const Products = (props) => {
  const [products, setProducts] = useState([]);
  const fetchProducts = async () => {
    const response = await fetch('http://localhost:8000/products/');
    const data = await response.json();
    setProducts(data);
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  const items = products.map(product=> <ProductItem key={product.id} id={product.id} title={product.title} price={product.price} description={product.description} />);
        
  return (
    <section className={classes.products}>
      <h2>Buy your favorite products</h2>
      <ul>
        {items}
      </ul>
    </section>
  );
};

export default Products;
