PROJECT=conall-sandbox
BUCKET=word_count_example_test

pytest --log-cli-level=INFO tests/pubsub_it_test.py --test-pipeline-options="--runner=TestDataflowRunner \
            --project=${{ PROJECT }} --region=europe-west1 \
            --staging_location=gs://${{ BUCKET }}/staging \
            --temp_location=gs://${{ BUCKET }}/temp \
            --job_name=it-test-pipeline \
            --setup_file ./setup.py"
