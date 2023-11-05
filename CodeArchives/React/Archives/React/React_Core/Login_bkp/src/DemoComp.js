import React from 'react';

const DemoComp = (props) => {
    console.log('LIST COMPONENT RUNNING');
    const ListComponent = <div>
    <ul>
       {
        props.items.map(
            (item) => <li key={Math.random().toString()}>{item}</li>
        )
       }
    </ul>
</div>

    return(
        <div>       
            {ListComponent}
        </div>
    );
};

export default React.memo(DemoComp);