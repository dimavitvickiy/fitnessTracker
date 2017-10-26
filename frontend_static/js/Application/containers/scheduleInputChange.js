import React from 'react'
import { connect } from 'react-redux'
import { scheduleInputChange } from '../actions'

let ScheduleInput = ({ dispatch }) => {
  let input;

  return (
    <div>
        <label>Type to change</label>
        <input
            className="form-control"
            onChange={e => {
                e.preventDefault();
                dispatch(scheduleInputChange(input.value));
            }}
            ref={node => {
                input = node
            }}
        />
    </div>
  )
};

ScheduleInput = connect()(ScheduleInput);

export default ScheduleInput;
