<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PsychJS Experiment</title>
  <!-- Include the PsychJS library -->
  <script src="https://cdn.jsdelivr.net/npm/psychjs"></script>
</head>
<body>
  <div id="experiment-container"></div>

  <script>
    // Define the experiment timeline
    const timeline = [
      {
        type: 'html-keyboard-response',
        stimulus: 'Press any key to start the experiment.'
      },
      {
        type: 'html-keyboard-response',
        stimulus: 'This is the first trial. Press any key to continue.'
      },
      {
        type: 'html-keyboard-response',
        stimulus: 'This is the second trial. Press any key to continue.'
      },
      {
        type: 'html-keyboard-response',
        stimulus: 'This is the final trial. Press any key to end the experiment.'
      },
      {
        type: 'html-keyboard-response',
        stimulus: 'Experiment complete! Thank you for participating.'
      }
    ];

    // Initialize the PsychJS experiment
    const experiment = new PsychExperiment({
      timeline: timeline,
      display_element: 'experiment-container',
      on_finish: function() {
        console.log('Experiment finished!');
      }
    });

    // Start the experiment
    experiment.start();
  </script>
</body>
</html>
