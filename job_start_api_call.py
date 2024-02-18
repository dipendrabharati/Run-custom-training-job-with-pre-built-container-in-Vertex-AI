# Import libraries
from google.cloud import aiplatform

# Initialize connection
aiplatform.init(location='europe-west1')

job = aiplatform.CustomPythonPackageTrainingJob(
    display_name='stroke_model_sdk',
    python_package_gcs_uri='gs://c4ds/vertexai/distributions/trainer-0.1.tar.gz',
    python_module_name='trainer.task',
    container_uri='europe-docker.pkg.dev/vertex-ai/training/scikit-learn-cpu.0-23:latest',
    staging_bucket='c4ds-europe-west1/vertexai/job_outputs'
)

job.run(
    replica_count=1, 
    machine_type='n1-standard-4',
    args=['--data_gcs_path=gs://datasets-c4ds/healthcare-dataset-stroke-data.csv']

)