while IFS="" read -r file || [ -n "$file" ]
do
  [[ $file =~ ^#.* ]] && continue
  rm -rf $file
  echo "$file Ignored from Deployment"
done < .deployignore