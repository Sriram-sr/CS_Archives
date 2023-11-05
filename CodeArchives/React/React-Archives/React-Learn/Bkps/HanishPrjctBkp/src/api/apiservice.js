import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const mieuproApi = createApi({
    reducerPath: 'pokemonApi',
    baseQuery: fetchBaseQuery({ baseUrl: 'https://pokeapi.co/api/v2/' }),
    endpoints: (builder) => ({
        getPokemonByName: builder.query({
            query: (name) => `pokemon/${name}`,
        }),
        getPokemonByType: builder.query({
            query: (type) => `type/${type}`
        }),
        registerUser: builder.mutation({
            query: (data) => ({
                url: '/register',
                method: 'POST',
                body: data
            })
        })
    }),
})

export const { useGetPokemonByNameQuery, useRegisterUserMutation, useGetPokemonByTypeQuery } = mieuproApi