import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec';

export default function() {
    const colors =  [
        '#df6b66',
        '#749aa0',
        '#e79d88',
        '#8cc1aa',
        '#ec7e55',
        '#72a375',
        '#efdd7d',
    ];
    // 政治面貌
    const politicalStatus = {
        title: '政治面貌',
        subtext: '共青团员: 1662人',
        legend: ['共产党员 1人', '少先队员 23人', '一般 78人', '民主党派 1人'],
        data: [1, 23, 78, 1],
    };
    // 民族
    const nationality = {
        title: '民族',
        subtext: '汉族: 1750人',
        legend: ['回族 2人', '满族 4人', '苗族 3人', '畲族 1人', '土家族 3人', '朝鲜族 2人'],
        data: [2, 4, 3, 1, 3, 2],
    };
    const option1 = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                axis: 'x',
                type: 'shadow',
            },
        },
        grid: {
            left: 0,
            right: 0,
            top: 0,
            bottom: '8%',
        },
        xAxis : {
            type : 'category',
            axisLine: {
                show: false
            },
            axisTick: {
                show: false
            },
            data : ['性别', '住宿', '年级']
        },
        yAxis : {
            show: false
        },
        series : [
            {
                type:'bar',
                stack: '1',
                itemStyle: {
                    color: colors[1],
                    barBorderRadius: [0,0,50,50]
                },
                label: {
                    show: true,
                    position: 'inside',
                    formatter: (params)=>{
                        if (params.value === 943) {
                            return '男生';
                        }
                        if (params.value === 708) {
                            return '住校';
                        }
                        if (params.value === 702) {
                            return '高一';
                        }
                        return '错误';
                    }
                },
                data:[943, 708, 702]
            },
            {
                type:'bar',
                stack: '1',
                itemStyle: {
                    color: colors[3],
                },
                label: {
                    show: true,
                    position: 'inside',
                    formatter: (params)=>{
                        if (params.value === 555) {
                            return '高二';
                        } else {
                            return '';
                        }
                    }
                },
                data:[NaN, NaN, 555]
            },
            {
                type:'bar',
                stack: '1',
                itemStyle: {
                    color: colors[0],
                    barBorderRadius: [50,50,0,0]
                },
                label: {
                    show: true,
                    position: 'inside',
                    formatter: (params)=>{
                        if (params.value === 822) {
                            return '女生';
                        }
                        if (params.value === 1057) {
                            return '走读';
                        }
                        if (params.value === 508) {
                            return '高三';
                        }
                        return '错误';
                    }
                },
                data:[822, 1057, 508]
            },
        ]
    }
    const getOption2 = (t) => {
        return {
            color: colors,
            title: {
                text: t.title,
                subtext: t.subtext,
                x: 'center',
                textStyle: {
                    fontSize: 14,
                    fontWeight: 400,
                },
            },
            legend: {
                bottom: 'bottom',
                right: 'right'
            },
            series : [
                {
                    type:'pie',
                    radius: [0, '70%'],
                    center : ['30%', '64%'],
                    hoverAnimation: false,
                    label: {
                        show: false
                    },
                    data: (function (l, d) {
                        let res = [];
                        for (let i = 0; i < l.length; i ++) {
                            res.push({value: d[i], name: l[i]});
                        }
                        return res;
                    }(t.legend, t.data)),
                }
            ]
        };
    };
    return (
        <Card>
            <Card.Header>
                <h4>1-1-2 人数比例</h4>
            </Card.Header>
            <Card.Body>
                <div className='row'>
                    <div className='col-12 col-lg-4'>
                        <Ec option={option1} h='300px'/>
                    </div>
                    <div className='col-12 col-lg-8'>
                        <div className='row'>
                            <div className='col-lg'>
                                <Ec option={getOption2(politicalStatus)} h='150px'/>
                            </div>
                        </div>
                        <div className='row'>
                            <div className='col-lg'>
                                <Ec option={getOption2(nationality)} h='150px'/>
                            </div>
                        </div>
                    </div>
                </div>
            </Card.Body>
        </Card>
    );
}
