import React from 'react';
import { Card , ProgressBar } from 'react-bootstrap';

function List(props) {
    return (
        <ul>
            {
                props.valArr.map((items, index) => {
                    let variant = '';
                    if (items < 40) {
                        variant = '0';
                    } else if (items < 45) {
                        variant = '1';
                    } else {
                        variant = '2';
                    }
                    return (
                        <li key={index} className='row ml-0 mr-0 mt-1 mb-1'>
                            <div className='col-12 col-lg-4 p-0'>{props.keyArr[index]}</div>
                            <div className='col-12 col-lg-8 p-0'>
                                <ProgressBar className='h-100' variant={variant} min={0} max={60} now={items} label={items + '人'} />
                            </div>
                        </li>
                    );
                })
            }
        </ul>
    );
}

export default function() {
    const CLASS_NAME = ['东-高一(01)', '东-高一(02)', '东-高一(03)', '东-高一(04)', '东-高一(05)', '东-高一(06)', '东-高一(07)', '东-高一(08)', '东-高一(09)-IB', '东-高一(10)-IB', '白-高一(01)', '白-高一(02)', '白-高一(03)', '白-高一(04)', '白-高一(05)', '白-高一(06)', '白-高一(07)', '白-高一(08)', '白-高二(01)', '白-高二(02)', '白-高二(03)', '白-高二(04)', '白-高二(05)', '白-高二(06)', '白-高二(07)', '白-高二(08)', '白-高二(09)', '白-高二(10)', '白-高二(12)', '高三(01)', '高三(02)', '高三(03)', '高三(04)', '高三(05)', '高三(06)', '高三(07)', '高三(08)', '高三(09)', '高三(10)', '高三(11)IB', '高三(12)IB', '高二(13)IB'];
    const CLASS_PEOPLE_NUMBER = [40, 40, 40, 40, 38, 33, 40, 40, 32, 33, 43, 43, 45, 43, 45, 46, 30, 30, 47, 44, 44, 44, 43, 45, 44, 40, 43, 43, 31, 47, 41, 42, 44, 44, 44, 42, 45, 41, 45, 37, 35, 57];
    return (
        <Card>
            <Card.Header>
                <h4>班级人数</h4>
            </Card.Header>
            <Card.Body>
                <div style={{height: '400px'}} className='overflow-y-scroll'>
                    <List keyArr={CLASS_NAME} valArr={CLASS_PEOPLE_NUMBER}/>
                </div>
            </Card.Body>
        </Card>
    );
}
