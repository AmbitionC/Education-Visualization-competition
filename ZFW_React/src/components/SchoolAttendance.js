import React from 'react';
import { Card } from 'react-bootstrap'
import Ec from './Ec';

export default function() {
    const xData = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
    const Data = [820, 932, 901, 934, 1290, 1330, 1320];
    const option = {
        xAxis: {
            type: 'category',
            data: xData},
        yAxis: {
            type: 'value'
        },
        series: [{
            data: Data,
            type: 'line'
        }]
    };
        return (
            <Card>
                <Card.Header>
                    <h4>考勤统计</h4>
                </Card.Header>
                <Card.Body>
                    <Ec option={option} h='400px'/>
                </Card.Body>
            </Card>
        )
}