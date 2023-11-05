import React from 'react'
import { useGetPokemonByNameQuery, useGetPokemonByTypeQuery } from '../api/apiservice'

const Test = () => {

    const { data: namedata, error: nameerror, isLoading: nameloading } = useGetPokemonByNameQuery('ditto');
    const { data: typedata, error: typeerror, isLoading: typeloading } = useGetPokemonByTypeQuery('3');
    console.log('Response for Type query', typedata);
    console.log('Response for Name query', namedata);
    console.log('Error Response for Name query', nameerror);
    console.log('Error Response for type query', typeerror);


    return (
        <div>
            <p>Test Component</p>
            {typeerror ? <p>{typeerror.status}</p> : <></>}
            {typeloading ? <h1>Loading...</h1> : (typedata ? <h1>{typedata.name}</h1> : <p>error while fetching data</p>)}
        </div>
    )
}

export default Test