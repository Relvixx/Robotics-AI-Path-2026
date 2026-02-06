read -p "Enter The Project Name" project_name

mkdir -p "$project_name"

mkdir -p "$project_name/src"
mkdir -p "$project_name/include"
mkdir -p "$project_name/config"

echo "# $project_name" > "$project_name/README.md" 
echo "Created by Rahul on $(date)" >> "$project_name/README.md" 

echo "------------------------------------------"
echo "✅ Project '$project_name' structure created!"
echo "📂 Location: $(pwd)/$project_name"
echo "------------------------------------------"