import React, { Component } from 'react';
import ThreeInSeven_1 from '../../components/Application3In71.js'
import ThreeInSeven_2 from '../../components/Application3In72.js'
import ThreeInSeven_3 from '../../components/Application3In73.js'
import ThreeInSeven_4 from '../../components/Application3In74.js'

export default function(){
    return (
        <React.Fragment>
            <div className='row mb-4'>
                <div className='col-12 col-lg-6'>
                    <ThreeInSeven_1 />
                </div>
                <div className='col-12 col-lg-6'>
                    <ThreeInSeven_2 />
                </div>
            </div>
            <div className='row mb-4'>
                <div className='col-12 col-lg-12'>
                    <ThreeInSeven_3 />
                </div>
            </div>
            <div className='row mb-4'>
                <div className='col-12 col-lg-12'>
                    <ThreeInSeven_4 />
                </div>
            </div>
        </React.Fragment>
    )
}