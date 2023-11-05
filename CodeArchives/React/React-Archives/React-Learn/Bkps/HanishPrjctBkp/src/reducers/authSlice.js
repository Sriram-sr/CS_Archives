import { createSlice } from '@reduxjs/toolkit';

export const AuthSlice = createSlice({
    name: 'Authentication',
    initialState: {
        auth: false
    },
    reducers: {
        registerUser: (state) => {
        }
    }
})