import React from "react";
import './Chart.css';
import Chartbar from './Chartbar';

const Chart = (props) => {
    const dataPointValues = props.dataPoints.map(dataPoint => dataPoint.value);
    const totalMaximum = Math.max(...dataPointValues);  
    return (
        <div className="chart">
            {
                props.dataPoints.map( (dataPoint) => {
                    return (
                        <Chartbar 
                        key={dataPoint.label} 
                        value={dataPoint.value}
                        maxValue={totalMaximum}
                        label={dataPoint.label}
                    />  
                    );
                })
            }
        </div>
    )
}

export default Chart;