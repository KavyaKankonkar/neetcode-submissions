class Solution {
public:
     void bubbleSort(vector<int>& nums,int len){
            int n=0;
            while(n<len-1){
            for(int i=0;i<len-1;i++){
                if(nums[i]>nums[i+1]){
                    int temp=nums[i];
                    nums[i]=nums[i+1];
                    nums[i+1]=temp;
                }
            }
            n++;
            }
           
        }

    vector<int> sortArray(vector<int>& nums) {
        int len=nums.size();

        bubbleSort(nums,len);
        return nums;
    }
};