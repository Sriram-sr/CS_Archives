import { Route, Switch, Redirect } from 'react-router-dom';
import AllQuotes from './pages/AllQuotes';
import QuoteDetail from './pages/QuoteDetail';
import NewQuote from './pages/NewQuote';
import { useState, useEffect } from 'react';
import Layout from './components/layout/Layout';
import NotFound from './components/quotes/NotFound';

function App() {
  const [quotes, setQuotes] = useState([]);
  const [isNewquote, setNewquote] = useState(false);
  useEffect(()=> {
    const fetchQuotes = async () => {
      const response = await fetch('http://localhost:8000/q/quotes/');
      const data = await response.json();
      setQuotes(data);
    };
  
    fetchQuotes();
  }, [isNewquote]);
  
  return (
    <Layout>
      <Switch>
        <Route path='/' exact>
          <Redirect to='/quotes' />
        </Route>
        <Route path='/quotes' exact>
          <AllQuotes quotes={quotes}/>
        </Route>
        <Route path='/quotes/:quoteId'>
          <QuoteDetail quotes={quotes}/>
        </Route>
        <Route path='/new-quote'>
          <NewQuote  setNewquote={setNewquote}/>
        </Route>
        <Route path='*'>
          <NotFound />
        </Route>
      </Switch>
    </Layout>
  );
}

export default App;
