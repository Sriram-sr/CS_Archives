import QuotesList from '../components/quotes/QuoteList';

const AllQuotes = (props) => {
    return (
        <QuotesList quotes={props.quotes} />
    );
};

export default AllQuotes;