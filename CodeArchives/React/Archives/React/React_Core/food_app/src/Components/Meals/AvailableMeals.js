import { useState, useEffect } from 'react';
import Card from '../UI/Card';
import './AvailableMeals.css';
import MealItem from './MealItem/MealItem';

const AvailableMeals = () => {
    const [meals, setMeals] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState();

    useEffect(()=>{
        const fetchData = async () => {
            const response = await fetch('http://192.168.0.109:8000/meals/');
            const data = await response.json();
            console.log(data);
            setMeals(data);
        };
        fetchData().catch(
            (error) => {
                setLoading(false);
                setError('Something Went wrong');
            }
        );
    }, [])
    // useEffect(() => {
    //     const fetchData = async () => {
    //         const tempMeals = [];
    //         // const response = await fetch('https://react-http-8b743-default-rtdb.firebaseio.com/meals.json');
    //         const response = await fetch('http://localhost:8000/meals/', { mode: 'no-cors'});
    //         const fetchedData = await response.json();
    //         console.log(fetchedData);
    //     //     for (const key in fetchedData) {
    //     //         tempMeals.push(
    //     //             {
    //     //                 id: key,
    //     //                 name: fetchedData[key].name,
    //     //                 description: fetchedData[key].description,
    //     //                 price: fetchedData[key].price
    //     //             }
    //     //         )
    //     //     }
        
    //     // setMeals(tempMeals);
    //     // setLoading(false);
    // }
    // fetchData().catch( (err) => {
    //     console.log(err.message);
    //     console.log('Error');
    //     // setLoading(false);
    //     // setError('Something went wrong');
    // } );
        //     try {

        //     }
        //     fetchData();
        // }catch (error) {
        //     setError(error.message || 'something went wrong...');
        // }
    // }, []);

    // if (loading) {
    //     return (
    //         <section className='loading'>
    //             <p>loading...</p>
    //         </section>
    //     );
    // }

    // if (error) {
    //     return (
    //         <section className='loading'>
    //             <p>{error}</p>
    //         </section>
    //     )
    // }
    const MealList = meals.map(meal => <MealItem key={meal.id} id={meal.id} price={meal.price} meal={meal.name} description={meal.description} />)
    return (            
        <section className="meals">
            <ul>
                <Card>
                    {MealList}
                </Card>
            </ul>
        </section>
    );
}

export default AvailableMeals;