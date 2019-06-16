import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec';
import Intro from './Intro';
import jsonData from '../data/app/sub_relative.json';

export default function() {

    const sub = ['语文', '数学', '英语', '物理', '化学', '生物', '政治', '历史', '地理', '技术'];

    const option1 = {
        tooltip: {
            formatter: param => ['线性相关度', sub[param.data[0]] + '-' + sub[param.data[1]], param.data[2].toFixed(2)].join('<br/>')
        },
        grid: {
            left: 0,
            right: '2%',
            top: '2%',
            bottom: 0,
            containLabel: true
        },
        xAxis: {
            type: 'category',
            data: sub,
            splitArea: {
                show: false
            },
            axisTick: {
                show: false
            },
            axisLine: {
                show: false
            },
            splitLine: {
                show: true,
                lineStyle: {
                    color: '#eeeeee',
                    type: 'dashed'
                }
            },
            axisLabel: {
                formatter: param => param[0] + '\n' + param[1]
            }
        },
        yAxis: {
            type: 'category',
            data: sub,
            splitArea: {
                show: false
            },
            axisTick: {
                show: false
            },
            axisLine: {
                show: false
            },
            splitLine: {
                show: true,
                lineStyle: {
                    color: '#eeeeee',
                    type: 'dashed'
                }
            }
        },
        visualMap: {
            show: false,
            min: 0.4,
            max: 0.5,
            inRange: {
                color: ['#fff','#df6b66']
            },
            outOfRange: {
                color: '#fff'
            }
        },
        series: [{
            name: '',
            type: 'heatmap',
            data: [[0, 1, 0.2126023828642828], [0, 2, 0.46456595689542735], [0, 3, 0.16429493752308943], [0, 4, 0.17365694412135446], [0, 5, 0.26008079961325015], [0, 6, 0.4469361728082814], [0, 7, 0.43109958940192256], [0, 8, 0.21999623711165595], [0, 9, 0.14053848740187203], [1, 2, 0.229398805557114], [1, 3, 0.4915518251186113], [1, 4, 0.386040044627757], [1, 5, 0.3209822717732279], [1, 6, 0.24260258834125048], [1, 7, 0.2660459185560523], [1, 8, 0.18937926770003755], [1, 9, 0.18767746955357845], [2, 3, 0.20832759391371802], [2, 4, 0.18438499613704262], [2, 5, 0.21930902967364826], [2, 6, 0.37054597064165506], [2, 7, 0.3101742237630789], [2, 8, 0.17030192305727754], [2, 9, 0.10791131851157508], [3, 4, 0.4517908047842244], [3, 5, 0.388748000829256], [3, 6, 0.21745951030540334], [3, 7, 0.2542762668593983], [3, 8, 0.2564702598210483], [3, 9, 0.13909828954476988], [4, 5, 0.49070708792220386], [4, 6, 0.22980670873489484], [4, 7, 0.21145452844406787], [4, 8, 0.3259403311623562], [4, 9, 0.1235113130148544], [5, 6, 0.31916001456487264], [5, 7, 0.2780310700033145], [5, 8, 0.4321450063009704], [5, 9, 0.22119882835539173], [6, 7, 0.45773872740702926], [6, 8, 0.2940580111470037], [6, 9, 0.1285895001110562], [7, 8, 0.33154414087694206], [7, 9, 0.1011659460504456], [8, 9, 0.15017336828324768]],
            itemStyle: {
                emphasis: {
                    shadowBlur: 5,
                    shadowColor: 'rgba(0, 0, 0, 0.2)'
                }
            }
        }]
    };

    const markLineOpt = (markLine) => {
        return {
            label: {
                show: false,
                position: 'middle',
                formatter: 'y=' + markLine['k'].toFixed(2) + '*x+' + markLine['b'].toFixed(2),
            },
            lineStyle: {
                normal: {
                    type: 'solid',
                    color: '#0b346e',
                    opacity: 0.6,
                    width: 1,
                }
            },
            emphasis: {
                label: {
                    show: true
                }
            },
            data: [[{
                coord: [0, markLine['b']],
                symbol: 'none'
            }, {
                coord: markLine['point'],
                symbol: 'none'
            }]]
        };
    };

    const getGrid = () => {
        let grid = [];
        for (let row = 0; row < 2; row ++) {
            for (let col = 0; col < 4; col ++) {
                grid.push({
                    left: (4 + col * 25) + '%',
                    top: (10 + row * 50) + '%',
                    width: '21%',
                    height: '32%',
                    containLabel: true
                });
            }
        }
        return grid;
    };
    
    const getAxis = (type) => {
        let axis = [];
        const name = {
            x: ['语文', '语文', '语文', '数学', '物理', '化学', '生物', '政治'],
            y: ['英语', '政治', '历史', '物理', '化学', '生物', '地理', '历史']
        };
        const nameLocation = {
            x: 'center',
            y: 'end'
        };
        for (let i = 0; i < 8; i ++) {
            axis.push({
                name: name[type][i],
                nameLocation: nameLocation[type],
                nameGap: 8,
                gridIndex: i,
                axisTick: {show: false},
                axisLabel: {show: false},
                splitLine: {
                    lineStyle: {
                        type: 'dashed',
                        color: '#eeeeee'
                    }
                }
            })
        }
        return axis;
    };

    const getSeries = () => {
        let series = [];
        const subMap = ['语文-英语', '语文-政治', '语文-历史', '数学-物理', '物理-化学', '化学-生物', '生物-地理', '政治-历史'];
        const markLine = [
            {'k': 0.7825488827332809, 'b': 17.44020449516519, 'point': [100, 95.69509276849328]},
            {'k': 0.7303677969324094, 'b': 21.24842352633786, 'point': [100, 94.2852032195788]},
            {'k': 0.7183256354000793, 'b': 22.06764352598848, 'point': [100, 93.9002070659964]},
            {'k': 0.700046570420584, 'b': 23.60111662175737, 'point': [100, 93.60577366381577]},
            {'k': 0.6739816490155985, 'b': 25.877860539278693, 'point': [100, 93.27602544083854]},
            {'k': 0.6842454001482101, 'b': 25.170908109292405, 'point': [100, 93.5954481241134]},
            {'k': 0.6229654010113441, 'b': 30.30323653739149, 'point': [100, 92.5997766385259]},
            {'k': 0.6967799929741674, 'b': 23.997364724009223, 'point': [100, 93.67536402142596]}
        ];
        for (let i = 0; i < 8; i ++) {
            series.push({
                type: 'scatter',
                xAxisIndex: i,
                yAxisIndex: i,
                symbolSize: 1,
                data: jsonData[subMap[i]],
                markLine: markLineOpt(markLine[i])
            });
        }
        return series;
    };
    
    const option2 = {
        color: ['#df6b66', '#90ca8f', '#e79d88', '#8cc1aa', '#749aa0', '#efdd7d', '#7189aa', '#71b9bc', '#F59F48'],
        grid: getGrid(),
        xAxis: getAxis('x'),
        yAxis: getAxis('y'),
        series: getSeries(),
    };
    return (
        <Card>
            <Card.Header>
                <h4>4-1-3 学科间的线性相关程度</h4>
                <Intro content={[
                    '左图: 以散点图的形式，展示全体学生的两学科成绩的分布，通过线性回归去拟合数据集',
                    '右图: 以热力图的形式，展示学科A与学科B的线性相关程度'
                ]} />
            </Card.Header>
            <Card.Body>
                <div className='row'>
                    <div className='col-12 col-lg-4'>
                        <Ec option={option2} h='360px' />
                    </div>
                    <div className='col-12 col-lg-1 align-items-center justify-content-center'>
                        <div className='right-arrow'></div>
                    </div>
                    <div className='col-12 col-lg-4'>
                        <Ec option={option1} h='360px' />
                    </div>
                    <div className='col-12 col-lg-1 align-items-center justify-content-center'>
                        <div className='right-arrow'></div>
                    </div>
                    <div className='col-12 col-lg-2 align-items-center'>
                        <span className='conclusion'><strong>结论：</strong>部分学科之间存在较强的线性相关性，充分利用这一点可以有效提高学生的成绩。若某学生数学成绩优异，但物理成绩不理想，由于数学和物理关联性较强，教师如果提供针对性帮助，该生的物理成绩提升空间极大</span>
                    </div>
                </div>
            </Card.Body>
        </Card>
    )
}