import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec';
import Intro from './Intro';
import kqJson1 from '../data/app/improve_kq_1.json';
import kqJson2 from '../data/app/improve_kq_2.json';
import kqJson3 from '../data/app/improve_kq_3.json';
import kqJson4 from '../data/app/improve_kq_4.json';
import kqJson5 from '../data/app/improve_kq_5.json';

export default function() {
    const getOption = (yMin, yMax, yName, series) => {
        return {
            tooltip: {
                formatter: param => param.data[2] ? ('学生ID: ' + param.data[2]) : ['迟到次数: ' + param.data[0], '比例: ' + param.data[1].toFixed(2)].join('<br/>')
            },
            grid: {
                left: 0,
                right: '2%',
                top: '16%',
                bottom: '12%',
                containLabel: true 
            },
            xAxis: {
                name: '迟到早退次数',
                nameLocation: 'center',
                nameGap: 28,
                axisTick: {
                    show: false
                },
                splitLine: {
                    show: false
                }
            },
            yAxis: {
                name: yName,
                min: yMin,
                max: yMax,
                axisTick: {
                    show: false
                },
                splitLine: {
                    lineStyle: {
                        color: '#eeeeee',
                        type: 'dashed'
                    }
                },
            },
            series: series
        };
    };
    const series1 = [{
        type: 'scatter',
        symbolSize: 3,
        itemStyle: {
            color: '#ec7e55'
        },
        data: kqJson1.data,
    }];
    const series2 = [{
        type: 'scatter',
        itemStyle: {
            color: '#71b8b9'
        },
        data: kqJson2.data,
    }, {
        type: 'line',
        showSymbol: false,
        smooth: true,
        itemStyle: {
            color: '#df6b66'
        },
        data: kqJson3.data,
    }];
    const series3 = [{
        type: 'scatter',
        itemStyle: {
            color: '#71b8b9'
        },
        data: kqJson4.data,
    }, {
        type: 'line',
        showSymbol: false,
        smooth: true,
        itemStyle: {
            color: '#df6b66'
        },
        data: kqJson5.data,
    }];
    return (
        <Card>
            <Card.Header>
                <h4>4-1-1 学生迟到早退次数和成绩的关系</h4>
                <Intro content={[
                    '左图: 以散点图的形式，展示学生的分布情况',
                    '右图: 针对不同的迟到早退次数，展示学生Z成绩为正的人数比例'
                ]} />
            </Card.Header>
            <Card.Body>
                <div className='row'>
                    <div className='col-12 col-lg-4'>
                        <Ec option={getOption(null, null, 'Z成绩', series1)} h='360px' />
                    </div>
                    <div className='col-12 col-lg-1 align-items-center justify-content-center'>
                        <div className='right-arrow'></div>
                    </div>
                    <div className='col-12 col-lg-4'>
                        <div className='row'>
                            <div className='col'>
                                <Ec option={getOption(0, 1, '优生比例', series2)} h='180px' />
                            </div>
                        </div>
                        <div className='row'>
                            <div className='col'>
                                <Ec option={getOption(0, 1, '差生比例', series3)} h='180px' />
                            </div>
                        </div>
                    </div>
                    <div className='col-12 col-lg-1 align-items-center justify-content-center'>
                        <div className='right-arrow'></div>
                    </div>
                    <div className='col-12 col-lg-2 align-items-center'>
                        <span className='conclusion'><strong>结论：</strong>若学生频繁的迟到或者早退，其成绩变差的概率会大幅度增加，班主任和校领导层注重学生考勤情况，加大管理力度</span>
                    </div>
                </div>
            </Card.Body>
        </Card>
    );
}
