BEGIN

  // Display the main options menu
  OUTPUT "Welcome to Langham Hotel Management System"
  OUTPUT "Select an operation:"
  OUTPUT "1. Add a New Room"
  OUTPUT "2. Remove an Existing Room"
  OUTPUT "3. View Room Information"
  OUTPUT "4. Book a Room"
  OUTPUT "5. Check Booking Status"
  OUTPUT "6. Generate Invoice & Free Room"
  OUTPUT "7. Save Booking Data to File"
  OUTPUT "8. Load Booking Data from File"
  OUTPUT "9. Backup Data and Clear File"
  OUTPUT "0. Exit Program"
  
  // Input user choice
  READ choice

  // Process the user input
  IF choice = 1 THEN
    // Add new room
    READ room_number, room_type, price, amenities_list
    IF room_number is valid AND room_number does not exist THEN
      ADD room to the room inventory
      OUTPUT "Room added successfully."
    ELSE
      OUTPUT "Invalid or duplicate room number."
    ENDIF
  ELSE IF choice = 2 THEN
    // Remove a room
    READ room_number
    IF room_number exists AND room is not booked THEN
      REMOVE room from the list
      OUTPUT "Room removed successfully."
    ELSE
      OUTPUT "Room not found or is currently booked."
    ENDIF
  ELSE IF choice = 3 THEN
    // Show room details
    IF no rooms in inventory THEN
      OUTPUT "No rooms are registered."
    ELSE
      FOR each room IN room_inventory
        OUTPUT room information
      END FOR
    ENDIF
  ELSE IF choice = 4 THEN
    // Room booking
    READ room_number, guest_name
    IF room_number available AND room is not booked THEN
      BOOK room for guest_name
      OUTPUT "Room booked successfully."
    ELSE
      OUTPUT "Room not available."
    ENDIF
  ELSE IF choice = 5 THEN
    // View booking status
    IF no bookings yet THEN
      OUTPUT "No current bookings."
    ELSE
      FOR each booking IN current_bookings
        OUTPUT booking details
      END FOR
    ENDIF
  ELSE IF choice = 6 THEN
    // Generate invoice and free room
    READ room_number
    IF room_number is booked THEN
      GENERATE invoice for booking
      RELEASE room for new bookings
      OUTPUT "Invoice generated and room freed."
    ELSE
      OUTPUT "Room is not booked."
    ENDIF
  ELSE IF choice = 7 THEN
    // Save booking data to a file
    IF current_bookings is not empty THEN
      OPEN file "LHMS_Studentid.txt" for writing
      SAVE booking details to file
      CLOSE file
      OUTPUT "Bookings saved to file successfully."
    ELSE
      OUTPUT "No bookings to save."
    ENDIF
  ELSE IF choice = 8 THEN
    // Load and display bookings from file
    OPEN file "LHMS_Studentid.txt" for reading
    IF file exists THEN
      READ and DISPLAY file content
    ELSE
      OUTPUT "Booking file not found."
    ENDIF
    CLOSE file
  ELSE IF choice = 9 THEN
    // Backup data and clear file content
    OPEN file "LHMS_Studentid.txt" for reading
    IF file exists AND file has data THEN
      CREATE backup file with current date-time
      COPY data to backup file
      DELETE content in original file
      CLOSE both files
      OUTPUT "Backup completed and file cleared."
    ELSE
      OUTPUT "No data to backup."
    ENDIF
  ELSE IF choice = 0 THEN
    // Exit the program
    OUTPUT "Exiting the program. Goodbye!"
    EXIT
  ELSE
    OUTPUT "Invalid choice. Please try again."
  ENDIF

END
