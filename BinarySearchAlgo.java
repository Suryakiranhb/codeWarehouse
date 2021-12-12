package com.practice.methods.gcd;

import java.util.Arrays;

public class BinarySearchAlgo {
		boolean binarySearch(int[] arr, int key) {
			int low =0;
			int high = arr.length-1;
			int mid;
			while(low<=high) {
					mid = (low+high)/2;
					if(arr[mid]==key) {
						return true;
					}
					else if(key<arr[mid]) {
						high = mid-1;
						low = low;
					}
					else {
						low=mid+1;
						high = high;
					}
					
				}
			return false;
		}
}
