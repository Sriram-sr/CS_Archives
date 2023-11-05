import { Route, useParams } from "react-router-dom";
import { Fragment } from "react";
import { useEffect, useState } from "react";
import Comments from '../components/comments/Comments';
import HighlightedQuote from '../components/quotes/HighlightedQuote';

const QuoteDetail = (props) => {
    const [quote, setQuote] = useState(null);
    const params = useParams();
    useEffect(() => {
        const quote = props.quotes.find(quote => quote.id === +params.quoteId);
        setQuote(quote);
    }, []);
    if(!quote){
        return <p>No Quote Found!!!</p>
    }
    return (
        <Fragment>
            {quote && <HighlightedQuote text={quote.text} author={quote.author}/>}
            <Route path='/quotes/:quoteId/comments'>
                <Comments />
            </Route>
        </Fragment>
    );
};

export default QuoteDetail;