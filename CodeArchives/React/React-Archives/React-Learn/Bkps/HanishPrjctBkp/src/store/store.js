import { configureStore } from '@reduxjs/toolkit'

import { mieuproApi } from '../api/apiservice'

export default configureStore({
    reducer: {
        [mieuproApi.reducerPath]: mieuproApi.reducer,
    },
    middleware: (getDefaultMiddleware) =>
        getDefaultMiddleware().concat(mieuproApi.middleware),

})