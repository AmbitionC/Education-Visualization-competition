import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec'

export default function(){
    const option = {

    };
    return (
        <Card>
            <Card.Header>
                <h4></h4>
            </Card.Header>
            <Card.Body>
                <Ec option={option} h='' />
            </Card.Body>
        </Card>
    )
}