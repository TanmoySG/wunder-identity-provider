while IFS="" read -r file || [ -n "$file" ]
do
  rm -rf $file
  echo "$file Ignored from Deployment."
done < .deployignore