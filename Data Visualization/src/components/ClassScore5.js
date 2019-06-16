import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec';
import Intro from './Intro';

export default function() {
    const stuRank = [[22, 33, '陈某某'], [23, 28, '慎某某'], [16, 28, '郑某某'], [22, 34, '徐某某'], [22, 27, '王某某'], [25, 34, '陈某某'], [17, 33, '孔某某'], [21, 26, '刘某某'], [20, 27, '唐某某'], [24, 31, '沈某某'], [26, 30, '赵某某'], [34, 29, '陈某某'], [30, 30, '朱某某'], [39, 37, '金某某'], [28, 27, '胡某某'], [33, 34, '许某某'], [36, 38, '康某某'], [37, 35, '裘某某'], [26, 28, '傅某某'], [28, 29, '王某某'], [28, 31, '缪某某'], [33, 40, '吴某某'], [38, 38, '李某某'], [33, 35, '夏某某'], [41, 37, '张某某'], [29, 24, '范某某'], [31, 24, '张某某'], [12, 19, '王某某'], [14, 17, '虞某某'], [10, 15, '李某某'], [14, 24, '周某某'], [20, 13, '沈某某'], [18, 23, '张某某'], [17, 18, '罗某某'], [17, 24, '励某某'], [22, 17, '胡某某'], [19, 23, '姜某某'], [15, 12, '柴某某'], [16, 15, '柳某某'], [12, 21, '师某某'], [21, 24, '诸某某'], [16, 7, '胡某某'], [23, 15, '符某某'], [22, 22, '陈某某'], [21, 22, '毕某某']];
    let dataset_1 = [];
    let dataset_2 = [];
    let dataset_3 = [];
    let dataset_4 = [];
    let data1 = [
        {name: '罗某某', itemStyle: {color: '#f59f48', borderColor: '#f59f48'}},
        {name: '柳某某', itemStyle: {color: '#f59f48', borderColor: '#f59f48'}},
        {name: '胡某某', itemStyle: {color: '#f59f48', borderColor: '#f59f48'}},
        {name: '李某某1', itemStyle: {color: '#f59f48', borderColor: '#f59f48'}},
        {name: '王某某', itemStyle: {color: '#f59f48', borderColor: '#f59f48'}},
        {name: '柴某某', itemStyle: {color: '#f59f48', borderColor: '#f59f48'}},
        {name: '虞某某', itemStyle: {color: '#f59f48', borderColor: '#f59f48'}},
        {name: '许某某', itemStyle: {color: '#df6b66', borderColor: '#df6b66'}},
        {name: '夏某某', itemStyle: {color: '#df6b66', borderColor: '#df6b66'}},
        {name: '吴某某', itemStyle: {color: '#df6b66', borderColor: '#df6b66'}},
        {name: '张某某', itemStyle: {color: '#df6b66', borderColor: '#df6b66'}},
        {name: '金某某', itemStyle: {color: '#df6b66', borderColor: '#df6b66'}},
        {name: '李某某2', itemStyle: {color: '#df6b66', borderColor: '#df6b66'}},
        {name: '康某某', itemStyle: {color: '#df6b66', borderColor: '#df6b66'}},
        {name: '裘某某', itemStyle: {color: '#df6b66', borderColor: '#df6b66'}},
    ];
    let links1 = [
        {source: '罗某某', target: '许某某', value: 1},
        {source: '柳某某', target: '夏某某', value: 1},
        {source: '胡某某', target: '吴某某', value: 1},
        {source: '李某某1', target: '张某某', value: 1},
        {source: '李某某1', target: '金某某', value: 1},
        {source: '王某某', target: '李某某2', value: 1},
        {source: '柴某某', target: '康某某', value: 1},
        {source: '虞某某', target: '裘某某', value: 1},
    ];
    let data2 = [
        {name: '沈某某1', itemStyle: {color: '#7189aa', borderColor: '#7189aa'}},
        {name: '符某某', itemStyle: {color: '#7189aa', borderColor: '#7189aa'}},
        {name: '胡某某1', itemStyle: {color: '#7189aa', borderColor: '#7189aa'}},
        {name: '毕某某', itemStyle: {color: '#7189aa', borderColor: '#7189aa'}},
        {name: '陈某某1', itemStyle: {color: '#7189aa', borderColor: '#7189aa'}},
        {name: '诸某某', itemStyle: {color: '#7189aa', borderColor: '#7189aa'}},
        {name: '范某某', itemStyle: {color: '#7189aa', borderColor: '#7189aa'}},
        {name: '张某某1', itemStyle: {color: '#7189aa', borderColor: '#7189aa'}},
        {name: '胡某某2', itemStyle: {color: '#7189aa', borderColor: '#7189aa'}},
        {name: '傅某某', itemStyle: {color: '#7189aa', borderColor: '#7189aa'}},
        {name: '陈某某2', itemStyle: {color: '#7189aa', borderColor: '#7189aa'}},
        {name: '赵某某', itemStyle: {color: '#7189aa', borderColor: '#7189aa'}},
        {name: '王某某1', itemStyle: {color: '#7189aa', borderColor: '#7189aa'}},
        {name: '朱某某', itemStyle: {color: '#7189aa', borderColor: '#7189aa'}},
        {name: '缪某某', itemStyle: {color: '#7189aa', borderColor: '#7189aa'}},
        {name: '师某某', itemStyle: {color: '#90ca8f', borderColor: '#90ca8f'}},
        {name: '周某某', itemStyle: {color: '#90ca8f', borderColor: '#90ca8f'}},
        {name: '郑某某', itemStyle: {color: '#90ca8f', borderColor: '#90ca8f'}},
        {name: '张某某2', itemStyle: {color: '#90ca8f', borderColor: '#90ca8f'}},
        {name: '励某某', itemStyle: {color: '#90ca8f', borderColor: '#90ca8f'}},
        {name: '姜某某', itemStyle: {color: '#90ca8f', borderColor: '#90ca8f'}},
        {name: '刘某某', itemStyle: {color: '#90ca8f', borderColor: '#90ca8f'}},
        {name: '唐某某', itemStyle: {color: '#90ca8f', borderColor: '#90ca8f'}},
        {name: '王某某2', itemStyle: {color: '#90ca8f', borderColor: '#90ca8f'}},
        {name: '慎某某', itemStyle: {color: '#90ca8f', borderColor: '#90ca8f'}},
        {name: '孔某某', itemStyle: {color: '#90ca8f', borderColor: '#90ca8f'}},
        {name: '沈某某2', itemStyle: {color: '#90ca8f', borderColor: '#90ca8f'}},
        {name: '陈某某3', itemStyle: {color: '#90ca8f', borderColor: '#90ca8f'}},
        {name: '徐某某', itemStyle: {color: '#90ca8f', borderColor: '#90ca8f'}},
        {name: '陈某某4', itemStyle: {color: '#90ca8f', borderColor: '#90ca8f'}},
    ];
    let links2 = [];
    for (let i = 0; i < 15; i ++) {
        links2.push({
            source: data2[i].name,
            target: data2[i+15].name,
            value: 1
        });
    }
    for (let i = 0; i < stuRank.length; i ++) {
        const singleData = stuRank[i];
        if (singleData[0] < 20 & singleData[1] < 20) {
            dataset_4.push(singleData);
        } else if (singleData[0] > 30 & singleData[1] > 30) {
            dataset_2.push(singleData);
        } else if ((singleData[0] + 1) / singleData[1] < 0.9) {
            dataset_1.push(singleData);
        } else {
            dataset_3.push(singleData);
        }
    }
    const option = {
        legend: {
            data: ['文理较优', '文优理劣', '文劣理优', '文理较劣']  
        },
        tooltip:{
            formatter: function (params) {
                return [
                    '学生：' + params.data[2],
                    '文科排名：' + params.data[0],
                    '理科排名：' + params.data[1]
                ].join('<br/>')
            }
        },
        grid: {
            left: '5%',
            right: '5%',
            top: '20%',
            bottom: '6%',
            containLabel: true
        },
        xAxis: {
            inverse: true,
            name: '文科排名',
            nameGap: 18,
            nameLocation: 'center',
            max: 50,
            min: 1,
            axisTick: {
                show: false
            },
            splitLine: {
                show: false
            }
        },
        yAxis: {
            inverse: true,
            name: '理科排名',
            nameGap: 18,
            nameLocation: 'start',
            max: 50,
            min: 1,
            axisTick: {
                show: false
            },
            splitLine: {
                lineStyle: {
                    color: '#eeeeee',
                    type: 'dashed'
                }
            }
        },
        series: [{
            name: '文优理劣',
            symbolSize: 10,
            data: dataset_1,
            itemStyle: {
                color: '#90ca8f'
            },
            type: 'scatter'
        },{
            name: '文理较劣',
            symbolSize: 10,
            data: dataset_2,
            itemStyle: {
                color: '#df6b66'
            },
            type: 'scatter'
        },{
            name: '文劣理优',
            symbolSize: 10,
            data: dataset_3,
            itemStyle: {
                color: '#7189aa'
            },
            type: 'scatter'
        },{
            name: '文理较优',
            symbolSize: 10,
            data: dataset_4,
            itemStyle: {
                color: '#f59f48'
            },
            type: 'scatter'
        }]
    };
    const sankeyOption = (data, links, method) => {
        return {
            tooltip: {
                formatter: (params) => {
                    const idx = params.name.indexOf('>');
                    if (idx > -1) {
                        return params.name.slice(0, idx) + method + params.name.slice(idx);
                    }
                    return params.name;
                 
                }
            },
            animation: false,
            series: [
                {
                    type: 'sankey',
                    top: '5%',
                    bottom: '5%',
                    left: '5%',
                    right: '5%',
                    draggable: false,
                    focusNodeAdjacency: false,
                    data: data,
                    links: links,
                    orient: 'vertical',
                    label: {
                        position: 'inside',
                        formatter: param => param.name[0],
                        color: '#ffffff'
                    },
                    lineStyle: {
                        normal: {
                            color: '#95aac9',
                        }
                    }
                }
            ]
        }
    }
    return (
        <Card>
            <Card.Header>
                <h4>2-5 班级帮扶</h4>
                <Intro content={[
                    '设计理念: 将班级学生分为4类，以散点图的形式展示，并给出班级内学生帮扶建议。A->B表示A帮助B，C<->D表示C和D互相帮助',
                    '功能: 帮助班主任去完成班内学生互相帮助，提高班级整体水平'
                ]} />
            </Card.Header>
            <Card.Body>
                <div className='row'>
                    <div className='col-12 col-lg-4'>
                        <Ec option={option} h='320px'/>
                    </div>
                    <div className='col-12 col-lg-3'>
                        <Ec option={sankeyOption(data1, links1, '-')} h='320px'/>
                    </div>
                    <div className='col-12 col-lg-5'>
                        <Ec option={sankeyOption(data2, links2, '<-')} h='320px'/>
                    </div>
                </div>
            </Card.Body>
        </Card>
    );
}