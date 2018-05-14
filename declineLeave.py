class DeclineLeave(Resource):
    @auth
    @cross_origin()
    def post():
        """Decline leave
        Args:
            application_id : the application id to decline
            leave_status: status of leave
            decline_reason: reason for declining leave
        """
       
        data = request.get_json(force=True)
        print(data)
        application_id = data['application_id']
        leave_status = data['LeaveStatus']
        decline_reason = data['DeclineReason']
        application_record = lms.applications.find_one({'application_id':application_id},{'_id':0})
        try:
            if application_record is None or application_record.leave_status != 'pending':
                return jsonify({'message': 'Cannot find this record in the database.'})
        except Exception as e:
            return jsonify({"succees":False,"error":e.__str__()}) 
        try:
            #application_record['leave_status']=leave_status
            lms.application_record.update(
            {'application_id':application_id},
            {
                '$push':
                {
                    'leave_status':'Rejected',
                    'decline_reason':decline_reason,
                    'date_reviewed'=str(datetime.now().date())
                }
            }
            )
        except Exception as e:
            return jsonify({"succees":False,"error":e.__str__()}) 

        # Send email
        send_email(
            application_record['email'], None, "Leave application declined",
            ("Your " + application_record['leave_type'] + " leave application for " + str(
                application_record['days']) + " day(s) from " +
            application_record['date_from'] + " to " + application_record['date_to'] +
            " has been declined. Reason for decline: " + decline_reason),
            file=None)

    return jsonify({'message': 'Leave has been declined.'})