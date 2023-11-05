import Header from "./components/layout/Header";
import { Provider } from "react-redux";
import store from "./store.js";

function App() {
  return (
    <Provider store={store}>
      <Header />
    </Provider>
  );
}

export default App;
