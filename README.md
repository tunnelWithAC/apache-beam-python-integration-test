## Apache Beam Integration Test Example

### Installation Steps
Create virtual environment

```
pip install --upgrade pip
pip install --upgrade virtualenv
pip install --upgrade setuptools

virtualenv ENV
. ENV/bin/activate
pip install apache-beam[gcp, test]
```

Set environment variables
```
BUCKET=
INPUT_SUB=
OUTPUT_TOPIC=
PROJECT=
REGION=europe-west1
```

### Run pipelines

Run pipeline using DirectRunner

```
python pipeline.py \
    --input_subscription "projects/$PROJECT/subscriptions/$INPUT_SUB" \
    --output_topic "projects/$PROJECT/topics/$OUTPUT_TOPIC"
```

Run pipeline using DataflowRunner

```
python porter_main.py \
  --setup_file ./setup.py \
  --region $REGION \
  --input_subscription "projects/$PROJECT/subscriptions/$INPUT_SUB" \
  --output_topic "projects/$PROJECT/topics/wordcount-output" \
  --runner DataflowRunner \
  --project $PROJECT \
  --temp_location gs://$BUCKET/tmp/ \
  --job_name my-new-dataflow-again \
  --enable-streaming-engine
```

Run integration test using TestDirectRunner

```
pytest --log-cli-level=INFO tests/pubsub_it_test.py --test-pipeline-options="--runner=TestDirectRunner \
    --project=$PROJECT --region=europe-west1 \
    --staging_location=gs://$BUCKET/staging \
    --temp_location=gs://$BUCKET/temp \
    --setup_file ./setup.py"
```

Run integration test using TestDataflowRunner
```
pytest --log-cli-level=INFO tests/pubsub_it_test.py --test-pipeline-options="--runner=TestDataflowRunner \
    --project=$PROJECT --region=europe-west1 \
    --staging_location=gs://$BUCKET/staging \
    --temp_location=gs://$BUCKET/temp \
    --job_name=it-test-pipeline \
    --setup_file ./setup.py"
```


# How to run other examples

### Wordcount Example
```
REGION=
BUCKET=
PROJECT=

python -m apache_beam.examples.wordcount \
  --region $REGION \
  --input gs://dataflow-samples/shakespeare/kinglear.txt \
  --output gs://$BUCKET/results/outputs \
  --runner DataflowRunner \
  --project $PROJECT \
  --temp_location gs://$BUCKET/tmp/
```
