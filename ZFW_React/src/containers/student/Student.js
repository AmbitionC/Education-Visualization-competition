import React, { Component } from 'react';
import StudentInfo from '../../components/StudentInfo1.js'
import StudentAttendance1 from '../../components/StudentAttendance1.js'
import StudentAttendance2 from '../../components/StudentAttendance2.js'
import StudentAttendance3 from '../../components/StudentAttendance3.js'
import StudentAttendance4 from '../../components/StudentAttendance4.js'
import StudentAttendance5 from '../../components/StudentAttendance5.js'

export default function(){
    return (
        <React.Fragment>
            <div className='row mb-4'>
                <div className='col-12 col-lg-2'>
                    <StudentInfo />
                </div>
                <div className='col- col-lg-5'>
                    <StudentAttendance1 />
                </div>
                <div className='col-12 col-lg-5'>
                    <StudentAttendance2 />
                </div>
            </div>
            <div className='row mb-4'>
                <div className='col-12 col-lg-4'>
                    <StudentAttendance3 />
                </div>
                <div className='col-12 col-lg-4'>
                    <StudentAttendance4 />
                </div>
                <div className='col-12 col-lg-4'>
                    <StudentAttendance5 />
                </div>
            </div>
        </React.Fragment>
    )
}