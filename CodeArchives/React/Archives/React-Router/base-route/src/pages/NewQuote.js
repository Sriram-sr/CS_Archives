import QuoteForm from '../components/quotes/QuoteForm';
import { useHistory } from 'react-router-dom';

const NewQuote = (props) => {
    const history = useHistory();
    const onAddQuote = async (quote) => {
        history.push('/quotes');
        const response = await fetch('http://localhost:8000/q/quotes/', {
            method: 'POST',
            body: JSON.stringify(quote),
            headers: {
                'Content-Type': 'application/json'
              }
        });
        const data = await response.json();
        console.log(data);
        props.setNewquote(true);
        // history.replace('quotes');
    };

    return (
        <QuoteForm onAddQuote={onAddQuote}/>
    );
};

export default NewQuote;