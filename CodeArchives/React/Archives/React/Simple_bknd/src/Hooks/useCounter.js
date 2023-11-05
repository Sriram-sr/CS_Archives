import { useState, useEffect } from 'react';

const useCounter = (increment = true) => {
    const [counter, setCounter] = useState(0);

    useEffect(
        () => {
            const interval = setInterval(
                () => {
                    if(increment){
                        setCounter( (prevCount)=> prevCount+1);
                    }else{
                        setCounter( (prevCount)=> prevCount-1);
                    }
                }, 1000
            )

            return () => clearInterval(interval);
        }, [increment]
    )

    return counter;
};

export default useCounter;