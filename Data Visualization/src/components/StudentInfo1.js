import React from 'react';
import { Card } from 'react-bootstrap';

export default function(){
    const dataArr = [
        {key: '性别', value:'女'},
        {key: '出生年份', value: '2002年'},
        {key: '民族', value: '汉族'},
        {key: '籍贯', value: '山西晋中'},
        {key: '政治面貌', value: '共青团员'},
        {key: '所在班级', value: '白-高二(01)'},
        {key: '是否住校', value: '住校'},
        {key: '寝室号', value: '604'},
        {key: '寝室人数', value: '4人'},
    ];
    const Content = (props) => {
        return (
            <React.Fragment>
                {
                    props.data.map((items, index) => {
                        const hr = index===0?<React.Fragment></React.Fragment>:<hr/>;
                        return (
                            <React.Fragment key={index}>
                                {hr}
                                <div className='row align-items-center'>
                                    <div className='col'>
                                        <h5 className='mb-0'>{items.key}</h5>
                                    </div>
                                    <div className='col-auto'>
                                        <small className='small text-muted'>{items.value}</small>
                                    </div>
                                </div>
                            </React.Fragment>
                        );
                    })
                }
            </React.Fragment>
        );
    }
    return (
        <Card>
            <Card.Header>
                <h4>3-1 个人信息</h4>
            </Card.Header>
            <Card.Body>
                <Content data={dataArr} />
            </Card.Body>
        </Card>
    )
}